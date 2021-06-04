from setuptools import setup

package_name = 'py_tdr3000'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mingyu',
    maintainer_email='ache159@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'tdr_3000 = py_tdr3000.tdr_3000:main',
        	'sir_2020 = py_sir2020.sir_2020:main',
        ],
    },
)
