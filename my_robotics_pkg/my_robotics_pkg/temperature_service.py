import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class TemperatureService(Node):

    def __init__(self):
        super().__init__('temperature_service')

        self.srv = self.create_service(
            AddTwoInts,
            'convert_temperature',
            self.convert_callback)

    def convert_callback(self, request, response):

        celsius = request.a
        fahrenheit = (celsius * 9/5) + 32

        response.sum = int(fahrenheit)

        self.get_logger().info(
            f"Converted {celsius}C -> {fahrenheit}F")

        return response


def main(args=None):
    rclpy.init(args=args)

    node = TemperatureService()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
