# Volatility
# Copyright (C) 2007-2013 Volatility Foundation
#
# This file is part of Volatility.
#
# Volatility is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License Version 2 as
# published by the Free Software Foundation.  You may not use, modify or
# distribute this program under any other version of the GNU General
# Public License.
#
# Volatility is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Volatility.  If not, see <http://www.gnu.org/licenses/>.
#

"""
@author:       Andrew Case
@license:      GNU General Public License 2.0
@contact:      atcuno@gmail.com
@organization:
"""

import volatility.obj as obj
import volatility.plugins.linux.common as linux_common

class linux_iomem(linux_common.AbstractLinuxCommand):
    """Provides output similar to /proc/iomem"""

    def yield_resource(self, io_res, depth = 0):

        if not io_res:
            #print "null"
            return []

        name = io_res.name.dereference_as("String", length = linux_common.MAX_STRING_LENGTH)
        start = io_res.start
        end = io_res.end

        output = [(depth, name, start, end)]

        output += self.yield_resource(io_res.child, depth + 1)
        output += self.yield_resource(io_res.sibling, depth)
        return output

    def calculate(self):

        def read_rel( offset, len_ ):
            return obj.Object("list_head", offset = device_private__device__ptr__addr - 152 + offset, vm = self.addr_space).obj_vm.read(addr = device_private__device__ptr__addr - 152 + offset, length = len_)

        def read_abs( offset, len_ ):
            return obj.Object("list_head", offset = offset, vm = self.addr_space).obj_vm.read(addr = offset, length = len_)


        linux_common.set_plugin_members(self)

        io_ptr = self.addr_space.profile.get_symbol("iomem_resource")
        io_res = obj.Object("resource", offset = io_ptr, vm = self.addr_space)

        io_pci_ptr = self.addr_space.profile.get_symbol("pci_bus_type")
        io_pci_res = obj.Object("bus_type", offset = io_pci_ptr, vm = self.addr_space)
        import struct

        # readin klist_devices->k_list->next pointer from SUBSYS_PRIVATE struct
        #---------------------------------------|------------------------------------------------------------------|----------------------------------------------|------|---|
        subsys__klist_devices__k_list__next__addr = struct.unpack('L', obj.Object("bus_type", offset = io_pci_res.p + 168 + 8, vm = self.addr_space).obj_vm.read(addr = io_pci_res.p + 168 + 8 , length = 8))[0]
        print "subsys__klist_devices__k_list__next__addr relies at--\t" + str(subsys__klist_devices__k_list__next__addr) + ";\thex =\t" + str(hex(subsys__klist_devices__k_list__next__addr))


        # so now we can get list_head *next pointer
        # get pointers
        device_private__n_node__next__addr = struct.unpack('L', obj.Object("list_head", offset = subsys__klist_devices__k_list__next__addr, vm = self.addr_space).obj_vm.read(addr = subsys__klist_devices__k_list__next__addr, length = 8))[0]
        print "device_private__n_node__next__addr list_head next relies at--\t" + str(device_private__n_node__next__addr) + ";\thex =\t" + str(hex(device_private__n_node__next__addr))
        device_private__n_node__prev__addr = struct.unpack('L', obj.Object("list_head", offset = subsys__klist_devices__k_list__next__addr + 8, vm = self.addr_space).obj_vm.read(addr = subsys__klist_devices__k_list__next__addr + 8, length = 8))[0]
        print "device_private__n_node__prev__addr prev relies at--\t" + str(device_private__n_node__prev__addr) + ";\thex =\t" + str(hex(device_private__n_node__prev__addr))
        start = device_private__n_node__next__addr
        resource_data = [];
        #========== start cycle of lookin at the devices classes ====look through the list==
        for i in range (150):
            print "\nRound {0}".format(i)

            # so now we can get list_head *next pointer

            # so now we can get struct device *device of a device_private structure

            device_private__device__ptr__addr = struct.unpack('L', obj.Object("list_head", offset = device_private__n_node__next__addr + 40, vm = self.addr_space).obj_vm.read(addr = device_private__n_node__next__addr + 40, length = 8))[0]
            print "device_private__device__ptr__addr relies at--\t" + str(device_private__device__ptr__addr) + ";\thex =\t" + str(hex(device_private__device__ptr__addr))

            #so now we can extract class
            pci_dev__class__ptr = struct.unpack('I', obj.Object("list_head", offset = device_private__device__ptr__addr - 152 + 68, vm = self.addr_space).obj_vm.read(addr = device_private__device__ptr__addr -152 + 68, length = 4))[0]
            print "class device\t" + str(hex(pci_dev__class__ptr)) #struct.unpack('I', obj.Object("list_head", offset = device_private__device__ptr__addr - 152 + 68, vm = self.addr_space).obj_vm.read(addr = device_private__device__ptr__addr - 152 + 68, length = 4)[0];

            for i in range(17):
                resource_data.append((struct.unpack('L', read_rel(888 + i*56, 8))[0],\
                                      struct.unpack('L', read_rel(888 + i*56 + 8, 8))[0],\
                                      struct.unpack('L', read_rel(888 + i*56 + 16, 8))[0] ))
                print resource_data[i]

            print "pointer to name " + str(struct.unpack('L', read_rel(152+80, 8))[0])
            # print obj.Object("list_head", offset = struct.unpack('L', read_rel(152+80, 8))[0], vm = self.addr_space).obj_vm.read(addr = struct.unpack('L', read_rel(152+80, 8))[0], length = 8)



            # resource_data.append(obj.Object("list_head", offset = device_private__n_node__next__addr - 152, vm = self.addr_space).obj_vm.read(addr = device_private__n_node__next__addr - 152, length = 2272))
            # print "device resources --\t" + str(resource_data) + ";\thex =\t" + str(hex(resource_data)) + "\n\n"

            # io_res
            device_private__n_node__next__addr = struct.unpack('L', obj.Object("list_head", offset = device_private__n_node__next__addr, vm = self.addr_space).obj_vm.read(addr = device_private__n_node__next__addr, length = 8))[0]
            print "next device_private struct pointer --\t" + str(device_private__n_node__next__addr) + ";\thex =\t" + str(hex(device_private__n_node__next__addr)) + "\n\n"
            if start == device_private__n_node__next__addr:
                break

        # import ipdb
        # ipdb.set_trace()

        # io_pci_dat

        # print "pci_bus_type output"
        #
        # print len(s)
        # dir(io_res)
        # dir(io_res.child)

        for r in self.yield_resource(io_res.child):
            yield r

    def render_text(self, outfd, data):
        dir(data)
        for output in data:
            depth, name, start, end = output

            #import pdb
            #pdb.set_trace()
            outfd.write("{0:35s}\t0x{1:<16X}\t0x{2:<16X}\n".format(("  " * depth) + name, start, end))
