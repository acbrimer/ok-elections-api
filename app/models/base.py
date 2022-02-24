from flask import jsonify, request, make_response
import json
from sqlalchemy.sql.expression import func
from .engine.app import db


class BaseModel:

    DEFAULT_SORT = ['id', 'ASC']

    @classmethod
    def getBaseQuery(cls):
        return cls.query

    @classmethod
    def getList(cls):
        page, perPage, sort, filter = cls.getListArgs()
        print(
            f"{cls.__name__}.getList: page={page} perPage={perPage} sort={sort} filter={filter}")
        q = cls.getBaseQuery()
        if sort[1] == 'DESC':
            q = q.order_by(getattr(cls, sort[0]).desc())
        else:
            q = q.order_by(getattr(cls, sort[0]))
        offset = (page - 1) * perPage
        q = q.offset(offset).limit(perPage)
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
        page = request.args.get('page', 1)
        if (isinstance(page, str)):
            try:
                page = int(page)
            except Exception as e:
                page = 1
        perPage = request.args.get('perPage', 10)
        if (isinstance(perPage, str)):
            try:
                perPage = int(perPage)
            except Exception as e:
                perPage = 10
        sort = request.args.get('sort', cls.DEFAULT_SORT)
        if (isinstance(sort, str)):
            try:
                sort = json.loads(sort)
                if (not isinstance(sort, list)):
                    sort = cls.DEFAULT_SORT
            except Exception as e:
                sort = cls.DEFAULT_SORT
        filter = request.args.get('filter', {})
        return page, perPage, sort, filter

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
