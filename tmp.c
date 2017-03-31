struct pci_dev {
	...
	unsigned int	class;  
	struct  device  dev;
	struct resource resource[];
	...
}

struct resource {
	resource_size_t start;
	resource_size_t end;
	...
};

struct bus_type {
…
struct subsys_private *p;
…
}
