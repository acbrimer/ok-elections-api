from flask import jsonify, request
from sqlalchemy.sql.expression import func
from .engine.app import db


class BaseModel:

    DEFAULT_SORT = 'id'
    DEFAULT_ORDER = 'ASC'

    @classmethod
    def getBaseQuery(cls):
        return cls.query

    @classmethod
    def getList(cls):
        page, perPage, sort, order, filter = cls.getListArgs()
        print(f"{cls.__name__}.getList: page={page} perPage={perPage} sort={sort} order={order} filter={filter}")
        q = cls.getBaseQuery()
        if order == 'DEC':
            q = q.order_by(getattr(cls, sort).desc())
        else:
            q = q.order_by(getattr(cls, sort))
        q = q.offset(page - 1 * perPage).limit(perPage)
        return jsonify({"data": cls.getListReponse(q.all()), "total": cls.count_star()})

    @classmethod
    def getOne(cls, resource_id):
        q = cls.getBaseQuery()
        return jsonify(q.filter_by(id=resource_id).first().toDict())

    @classmethod
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
        order = request.args.get('order', cls.DEFAULT_ORDER)
        filter = request.args.get('filter', {})
        return page, perPage, sort, order, filter

    @classmethod
    def count_star(cls):
        q = db.session.query(
            func.count(cls.id)
        )
        return q.scalar()

    @staticmethod
    def getListReponse(queryResults):
        return [r.toDict() for r in queryResults]

    def toDict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)
        return d
