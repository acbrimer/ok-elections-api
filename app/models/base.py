from flask import jsonify, request, make_response
import json
from sqlalchemy.sql.expression import func
from .engine.app import db


class BaseModel:

    DEFAULT_SORT = ['id', 'ASC']
    DEFAULT_RANGE = [0, 9]

    @classmethod
    def getBaseQuery(cls):
        return cls.query

    @classmethod
    def getList(cls):
        range, sort, filter = cls.getListArgs()

        print(
            f"{cls.__name__}.getList: range={range} sort={sort} filter={filter}")
        q = cls.getBaseQuery()
        if sort[1] == 'DESC':
            q = q.order_by(getattr(cls, sort[0]).desc())
        else:
            q = q.order_by(getattr(cls, sort[0]))
        # apply offset and limit if range != [0, 0]
        if (range[0] != 0 or range[1] != 0):
            offset = range[0]
            limit = (range[1] - range[0]) + 1
            q = q.offset(offset).limit(limit)
        total = cls.count_star()
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
        return range, sort, filter

    @ classmethod
    def count_star(cls):
        q = db.session.query(
            func.count(cls.id)
        )
        return q.scalar()

    @ staticmethod
    def getListReponse(queryResults):
        return [r.toDict() for r in queryResults]

    def toDict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)
        return d
