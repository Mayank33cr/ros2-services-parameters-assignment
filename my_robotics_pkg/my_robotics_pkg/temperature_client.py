import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class TemperatureClient(Node):

    def __init__(self):
        super().__init__('temperature_client')

        self.client = self.create_client(
            AddTwoInts,
            'convert_temperature')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available...')

        self.req = AddTwoInts.Request()

    def send_request(self, celsius):

        self.req.a = celsius
        self.req.b = 0

        self.future = self.client.call_async(self.req)


def main(args=None):

    rclpy.init(args=args)

    client = TemperatureClient()

    client.send_request(25)

    rclpy.spin_until_future_complete(client, client.future)

    result = client.future.result()

    client.get_logger().info(
        f"Temperature in Fahrenheit: {result.sum}")

    rclpy.shutdown()


if __name__ == '__main__':
    main()
