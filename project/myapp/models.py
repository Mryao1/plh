from django.db import models

# Create your models here.
class UserInfo(models.Model):#用户信息
    UserNo = models.EmailField(unique=True)#邮箱
    UserName = models.CharField(max_length=15)
    Password  = models.SlugField(max_length=16)#只允许减号、下划线、字母、数字
    Phone = models.CharField(max_length=11)
    Freetimes =models.IntegerField(default=6)#免费次数
    Identify = models.CharField(choices=(('个人','个人'),('公司','公司')),default='个人',max_length=3)
#choice里由(value,display_name)组成
#通过属性取value，通过 get_属性_display()方法取display_name
    def __str__(self):
        return "   用户名："+self.UserName
class Plant(models.Model):
    PlantName = models.CharField(max_length=30,primary_key=True) 
    ControlMethod = models.TextField()
    Picture =models.ImageField(upload_to='PlantPic')
    def __str__(self):
        return self.PlantName   
class PlantDisease(models.Model):
    PlantName = models.ForeignKey(Plant, related_name='plantname',on_delete=models.CASCADE)
    DiseaseName = models.CharField(max_length=15)
    #Morbidity =models.CharField(max_length=15)
#html界面中显示数据库TextField类型数据时需要在末尾加  |linebreaksbr  ，否则文本显示不会换行
#eg：{{item.PreMeasures|linebreaksbr}}    item为数据库中的一行
    Symptoms = models.TextField()
    PreMeasures = models.TextField()
    Img = models.ImageField(upload_to='img')#需要修改配置
    def  __str__(self):
         return self.PlantName.PlantName+self.DiseaseName
