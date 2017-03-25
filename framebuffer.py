import volatility.obj as obj
import volatility.plugins.linux.common as linux_common

class linux_iomem(linux_common.AbstractLinuxCommand):
    """Provides output similar to /proc/iomem"""

    def yield_resource(self, io_res, depth = 0):


	def calculate(self):

		def read_rel( offset, len_ ):
			return obj.Object("list_head", offset = device_private__device__ptr__addr - 152 + offset, vm = self.addr_space).obj_vm.read(addr = device_private__device__ptr__addr - 152 + offset, length = len_)


		def read_abs( offset, len_ ):
			return obj.Object("list_head", offset = offset, vm = self.addr_space).obj_vm.read(addr = offset, length = len_)

		for r in self.yield_resource(io_res.child):
				yield r


		def render_text(self, outfd, data):
			dir(data)
			for output in data:
				depth, name, start, end = output

				#import pdb
				#pdb.set_trace()
				outfd.write("{0:35s}\t0x{1:<16X}\t0x{2:<16X}\n".format(("  " * depth) + name, start, end))
