# import json
# from App.Repositories.user_repository import UserRepository
# from App.Database.schemas import User
# from pydantic_sqlalchemy import sqlalchemy_to_pydantic

# def objectKeyExist(key, obj):
#     dict_json = json.dumps(obj)
#     if key in dict_json:
#         return True
#     return False


# def checkInstance(obj, myClass):
#     if isinstance(obj, myClass):
#         return True
#     return False


# def test_user_repository_query_all(db_session):
#     userRepository = UserRepository()
#     users = userRepository.all()
#     user_json = userRepository.to_dict(users[0])

#     assert len(users) >= 1
#     assert checkInstance(users[0], User) is True
#     assert objectKeyExist('id', user_json) is True

