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


system.map:
ffffffff81aa8360 D pci_bus_type
ffffffff81aa8360 - address

000000000000a020 D cpu_llc_id
000000000000a040 D cpu_llc_shared_map
000000000000a080 D cpu_core_map
000000000000a0c0 D cpu_sibling_map
000000000000a100 D cpu_info
000000000000a1e0 D cpu_number
000000000000a1e8 D this_cpu_off
000000000000a1f0 D x86_cpu_to_apicid
000000000000a1f2 D x86_bios_cpu_apicid
000000000000a200 d cpu_loops_per_jiffy
000000000000a240 d pmc_prev_left
000000000000a440 D cpu_hw_events
000000000000b700 d bts_ctx

BUILD OWN PROFILE
✓ Module.dwarf
✓ System.map
✓ Load built profile
✓ Ready for stage 2
