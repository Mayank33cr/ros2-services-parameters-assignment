from setuptools import find_packages, setup

package_name = 'my_robotics_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='turtle',
    maintainer_email='turtle@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
'temperature_service = my_robotics_pkg.temperature_service:main',
        'temperature_client = my_robotics_pkg.temperature_client:main',
        'parameter_publisher = my_robotics_pkg.parameter_publisher:main',
        ],
    },
)
