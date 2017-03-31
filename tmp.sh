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

01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Caicos XTX [Radeon HD 8490 / R5 235X OEM] (prog-if 00 [VGA controller])
	Subsystem: Hewlett-Packard Company Caicos XTX [Radeon HD 8490 / R5 235X OEM]
	Flags: bus master, fast devsel, latency 0, IRQ 27
	Memory at e0000000 (64-bit, prefetchable) [size=256M]


