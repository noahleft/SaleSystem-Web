#!/usr/local/bin/python3

# genOptions
# return the datalist in html option format
# datalist is a list consist of data tuples like (1,'a'),(2,'b')
# an example datalist is [(1,'a'),(2,'b')]
# the first element in the tuple means the value which is the index of the selected data
# the second element in the tuple means the display value which is the values user would see
def genOptions(dataList,initial=1):
  strList=[]
  optionStr=lambda x:'<option value="'+str(x[0])+'">'+str(x[1])+'</option>'
  optionStrSelected=lambda x:'<option value="'+str(x[0])+'" selected>'+str(x[1])+'</option>'
  for data in dataList:
    if data[0]==initial:
      strList.append(optionStrSelected(data))
    else:
      strList.append(optionStr(data))
  return '\n'.join(list(strList))


