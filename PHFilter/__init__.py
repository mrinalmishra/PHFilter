#!/usr/bin/env python
# -*- coding: utf-8 -*-


################################################################################################################
#                                                                                                              #
# Copyright (C) {2014}  {Mrinal Mishra, Miyamoto lab, Biology Department, University of Florida}      #
#                                                                                                              #
# This program is free software: you can redistribute it and/or modify                                         #
# it under the terms of the GNU General Public License as published by                                         #
# the Free Software Foundation, either version 3 of the License, or                                            #
# (at your option) any later version.                                                                          #
#                                                                                                              #
# This program is distributed in the hope that it will be useful,                                              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of                                               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                                #
# GNU General Public License for more details.                                                                 #
#                                                                                                              #
# This program comes with ABSOLUTELY NO WARRANTY;                                                              #
# This is free software, and you are welcome to redistribute it                                                #
# under certain conditions;                                                                                    #
#                                                                                                              #
################################################################################################################
name = "PHFilter"
__author__ = "Mrinal Mishra <mrinalmishra@.ufl.edu>"
__date__ = "1st March 2019"
__version__ = "1.0"


class PHF():
    def execute(self, input_file, output_file, heterozygous_cutoff=1):
        fdata = open(input_file, "rU")
        with open(output_file, "w") as fp:
            for lines in fdata:
                lobj = lines.strip().split("\t")
                if "#" not in lobj[0]:
                    count_01 = 0
                    count_11 = 0
                    elemnts = lobj[9:]
                    for in_element in elemnts:
                        elObj = in_element.split(":")
                        if elObj[0] == "0/1":
                            count_01 = count_01 + 1
                        if elObj[0] == "1/1":
                            count_11 = count_11 + 1

                    if count_01 == heterozygous_cutoff and count_11 == 0:
                        continue
                    else:
                        fp.write(lines)

                else:
                    fp.write(lines)


