from flask_sqlalchemy import SQLAlchemy
import time


db = SQLAlchemy()


def timestamp():
    format = '%Y/%m/%d'
    dt = time.strftime(format,time.localtime())
    return dt


class ModelMixin(object):
    @classmethod
    def new(cls, form,**kwargs):
        m = cls(form)
        for k,v in kwargs.items():
            setattr(m,k,v)
        m.save()
        return m

    @classmethod
    def update(cls, model_id, form):
        m = cls.query.get(model_id)
        print('update cls method', m, model_id)
        m._update(form)
        m.save()

    @classmethod
    def delete(cls, model_id):
        m = cls.query.get(model_id)
        m.remove()

    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0} = {1}'.format(k, v) for k, v in self.__dict__.items())
        return '<{0}: \n  {1}\n>'.format(class_name, '\n  '.join(properties))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

