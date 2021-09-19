import abc
from App.Http.Responses.pagination_response import PaginationResponse

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def to_dict(self, obj):
        raise NotImplementedError

    @abc.abstractmethod
    def to_list(self, l):
        raise NotImplementedError



class BaseRepository(AbstractRepository):

    _model = None

    def __init__(self):
        pass

    def paginate(self, per_page: int=10, page: int=1):
        pagination_data = self._model.paginate(per_page, current_page=page)
        return self._formatted_paginate(pagination_data)

    def find(self, id: int):
        item = self._model.find(id)
        if item is not None:
            return item.serialize()
        return None

    def create(self, request):
        item = self._model.create(request)
        if item is not None:
            return item.serialize()
        return None

    def update(self, id: int, request):
        data = request.dict(
            exclude_none=True,
            exclude_unset=True,
            exclude_defaults=True,
        )
        item = self._model.find(id)
        if item is not None:
            item.update(data)
            return item.serialize()
        return None

    def delete(self, id: int):
        item = self._model.find(id)
        if item is not None:
            item.delete()
            return True
        return None     
    
    def to_dict(self, obj):
        if obj is not None:
            return {c.key: getattr(obj, c.key)
                for c in inspect(obj).mapper.column_attrs}
        else:
            return {}

    def to_list(self, _list):
        if isinstance(_list, list) and len(_list):
            output = []
            for item in _list:
                output.append(self.to_dict(item))
            return output
        else:
            print("A list is reuired!")
            return []
 
    def _formatted_paginate(self, results):
        return PaginationResponse(
            total = results.total,
            per_page = results.per_page,
            last_page = results.last_page,
            current_page = results.current_page,
            data = results.serialize()
        )

    def _is_empty(self, value):
        if value is None:
            return True
        elif isinstance(value, str) and value.strip() == '':
            return True
        return False


        