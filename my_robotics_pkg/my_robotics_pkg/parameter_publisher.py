import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ParameterPublisher(Node):

    def __init__(self):
        super().__init__('parameter_publisher')

        self.declare_parameter('publish_text', 'Hello ROS2')

        self.publisher = self.create_publisher(
            String,
            'parameter_topic',
            10)

        timer_period = 2.0

        self.timer = self.create_timer(
            timer_period,
            self.timer_callback)

    def timer_callback(self):

        text = self.get_parameter(
            'publish_text').get_parameter_value().string_value

        msg = String()

        msg.data = text

        self.publisher.publish(msg)

        self.get_logger().info(f"Publishing: {text}")


def main(args=None):

    rclpy.init(args=args)

    node = ParameterPublisher()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
