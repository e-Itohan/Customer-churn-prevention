from setuptools import find_packages, setup

setup(

    name='Customer churn prevention',
    version='0.0.1',
    author='Eniola',
    url='https://github.com/e-Itohan/Customer-churn-prevention',
    packages=find_packages,
    install_requires=['jupyterlab','pillow', 'matplotlib', 'seaborn', 'libquadmath',
                      'pandas', 'scikit-learn', 'python-dotenv', 'psycopg2-binary', 
                      'SQLAlchemy', 'xgboost', 'keras', 'scikeras', 'tensorflow', 'np_utils']

)
