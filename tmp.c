struct device_private {
	...
	struct klist_node knode_bus;
	struct device *device;
	...
};