#!/usr/bin/env python3
"""
DIGITAL TWIN NODE
- Maintains robot joint state
- Broadcasts TF
- Acts as single source of truth
"""

import rclpy
from rclpy.node import Node


class DigitalTwinNode(Node):
    def __init__(self):
        super().__init__('digital_twin_node')
        self.get_logger().info('Digital Twin initialized')


def main(args=None):
    rclpy.init(args=args)
    node = DigitalTwinNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
