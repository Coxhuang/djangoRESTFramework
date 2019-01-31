from rest_framework.viewsets import mixins
from rest_framework.viewsets import GenericViewSet
from app import models
from app.user.new.newclasses.newclassesserializer import newclassesserializer




"""
1. 班级   新增 / 删除 / 修改 / 查看列表 / 查看详细信息
"""
class newclassesview(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     GenericViewSet):

    serializer_class = newclassesserializer
    queryset = models.Classes.objects.all()


    def get_queryset(self):

        """逻辑代码"""
        return models.Classes.objects.all()

