# python虚拟环境配置
> - 需要安装多个Python环境
> - 解决不同项目依赖库的冲突
> - 隔离项目环境，防止污染
> - virtualenv 与 virtualenvwrapper

## 安装pip
curl https://bootstrap.pypa.io/get-pip.py | python3
pip --version

## 安装 virtualenv
pip install virtualenv

## 创建虚拟环境
> - 建议每创建一个项目，就给其自己创建一个虚拟环境
> - 创建一个工程目录
```
mkdir test
cd test (自定义工作目录)
where python3
// /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
1.virtualenv -p /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 py3(自定义虚拟环境名称，也可以改成其他的比如py3)
这时，在工作目录test下就创建了一个python3的文件夹，python3虚拟环境就创建好了
2.激活虚拟环境
source python3/bin/activate
这样安装其他相关的依赖库则可以使用pip来安装
3.工作完后，需要退出虚拟环境，否则会影响其他环境
deactivate
```
![](readImg/virtualenv.png)

## jupyter
> pip install jupyter
> jupyter notebook  就可以浏览器编译了