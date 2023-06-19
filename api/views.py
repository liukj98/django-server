from django.http import HttpResponse

def keyGeneration(request):
  print(request.GET.get("keyGenAlg"))
  # 拿到前端传来的参数
  # 调用对应算法，得到结果然后返回
  return HttpResponse("key Generation hahha")