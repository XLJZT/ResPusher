import setuptools

setuptools.setup(
    name="ResPusher", # 替换为你的包/项目名
    version="0.1.0", # 替换为你的当前项目版本
    author="XLJZT", # 替换为你的名字
    author_email="xljzts@163.com", # 替换为你的邮箱
    description="通过微信发送自己实验的结果", # 替换为你的项目简介
    long_description=open('README.md').read(), # 从README.md文件中获取长描述
    long_description_content_type="text/markdown", # 长描述的内容类型
    url="https://github.com/XLJZT/ResPusher", # 替换为你的项目的仓库url
    packages=setuptools.find_packages(), # 自动发现项目中的包
    install_requires=['requests'], # 你的项目需要的第三方库
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6', # 你的项目需要的Python版本
)