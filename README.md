# binbox
python命令执行小工具
[follow](https://github.com/forMwish/binbox)
## 安装

```bash
tar -zxvf binbox.tar.gz
cd binbox
pip install -r requirement.txt
pip install setuptools
python setup.py develop
```

## 打包whl文件
```bash
tar -zxvf binbox.tar.gz
cd binbox
pip install -r requirement.txt
pip install setuptools
python setup.py bdist_wheel
cd dist && pip install binbox-1.0-py3-none-any.whl
```
