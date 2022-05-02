# 时间戳与时间字符串转换工具

### 说明
```shell script
ts
```
```
usage: ts [-h] [-p FORMATED_STR] [-f TIMESTAMP] [-n]

时间戳与时间字符串转换工具

optional arguments:
  -h, --help            show this help message and exit
  -p FORMATED_STR, --parse FORMATED_STR
                        parse formated str to timestamp
  -f TIMESTAMP, --format TIMESTAMP
                        format timestamp to str
  -n, --now             get now info
```

### 当前时间
```shell script
ts -n 
```  
```
1651469104
1651469104685
1651469104685354
2022-05-02 13:25:04
```                   

### 获取时间戳
```shell script
ts -p "2022-05-02 00:00:00"
```
```
1651420800
```

### 格式化时间戳
```shell script
ts -f 1651388100 
```
```
2022-05-01 14:55:00   
```

### Build(on Mac)
```shell script
./install.sh
./build.sh
```