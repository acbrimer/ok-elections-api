from flask import jsonify, request, make_response
import json
from sqlalchemy import func
from .engine.app import db
from datetime import datetime


class BaseModel:

    DEFAULT_SORT = ['id', 'ASC']
    DEFAULT_RANGE = [0, 9]

    @classmethod
    def load_dataframe(cls, df, column_mappings=None, if_exists='append'):
        print(f"{cls.__name__}.load_dataframe: {len(df.index)} rows")
        if column_mappings:
            df.rename(columns=column_mappings, inplace=True)
        dropDFColumns = [c for c in df.columns if not hasattr(cls, c)]
        if len(dropDFColumns) > 0:
            df.drop(columns=dropDFColumns, inplace=True)
            dropDFColumns = ", ".join(dropDFColumns)
            print(f"  Dropped DF columns: {dropDFColumns}")
        missingTableCols = [
            c.name for c in cls.__table__.columns if not c.name in df.columns]
        if missingTableCols:
            missingTableCols = ", ".join(missingTableCols)
            print(f"  Missing Table columns: {missingTableCols}")
        try:
            df.to_sql(cls.__tablename__, if_exists=if_exists,
                      index=False, con=db.engine)
            return {"rows": cls.count_star()}
        except Exception as e:
            return {"error": e}

    @classmethod
    def getBaseQuery(cls):
        return cls.query

    @classmethod
    def applyFilters(cls, q, filter):
        for col, value in filter.items():
            if col in cls.__table__.columns:
                # apply 'in' filters
                c = cls.__table__.columns[col]
                t = c.__dict__['type']
                if (isinstance(value, list)):
                    q = q.filter(c.in_(value))
                # apply simple scalar filters to columns
                if not isinstance(value, dict):
                    # apply LIKE %% query for varchar
                    if (str(t).startswith('VARCHAR')):
                        q = q.filter(c.like(f'%{value}%'))
                    elif (str(t).startswith('DATE')):
                        q = q.filter(func.DATE(c) == value)
                    else:
                        q = q.filter(c == value)
                else:
                    print('handle dict filters')
        return q

    @classmethod
    def getList(cls):
        range, sort, filter = cls.getListArgs()
        print(
            f"{cls.__name__}.getList: range={range} sort={sort} filter={filter}")
        q = cls.getBaseQuery()
        q = cls.applyFilters(q, filter)
        total = cls.count_star(filter)
        if sort[1] == 'DESC':
            q = q.order_by(getattr(cls, sort[0]).desc())
        else:
            q = q.order_by(getattr(cls, sort[0]))
        # apply offset and limit if range != [0, 0]
        if (range[0] != 0 or range[1] != 0):
            offset = range[0]
            limit = (range[1] - range[0]) + 1
            q = q.offset(offset).limit(limit)
        print(q.statement.compile(compile_kwargs={"literal_binds": True}))
        response = make_response(jsonify(cls.getListReponse(q.all())))
        response.headers.add("X-Total-Count", total)
        return response

    @ classmethod
    def getOne(cls, resource_id):
        q = cls.getBaseQuery()
        return jsonify(q.filter_by(id=resource_id).first().toDict())

    @ classmethod
    def getListArgs(cls):
        range = request.args.get('range', cls.DEFAULT_RANGE)
        if (isinstance(range, str)):
            try:
                range = json.loads(range)
                if (not isinstance(range, list)):
                    range = cls.DEFAULT_RANGE
            except Exception as e:
                range = cls.DEFAULT_RANGE

        sort = request.args.get('sort', cls.DEFAULT_SORT)
        if (isinstance(sort, str)):
            try:
                sort = json.loads(sort)
                if (not isinstance(sort, list)):
                    sort = cls.DEFAULT_SORT
            except Exception as e:
                sort = cls.DEFAULT_SORT
        filter = request.args.get('filter', {})
        if (isinstance(filter, str)):
            try:
                filter = json.loads(filter)
                if (not isinstance(filter, dict)):
                    filter = {}
            except Exception as e:
                filter = {}
        return range, sort, filter

    @ classmethod
    def count_star(cls, filter={}):
        q = db.session.query(
            func.count(cls.id)
        )
        if len(filter.keys()) > 0:
            q = cls.applyFilters(q, filter)
        return q.scalar()

    @ staticmethod
    def getListReponse(queryResults):
        return [r.toDict() for r in queryResults]

    def toDict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)
        return d
