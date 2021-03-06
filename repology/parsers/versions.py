# Copyright (C) 2018 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# This file is part of repology
#
# repology is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# repology is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with repology.  If not, see <http://www.gnu.org/licenses/>.


__all__ = ['VersionStripper']


class VersionStripper():
    def __init__(self):
        self.strips = []

    def strip_left(self, separator):
        self.strips.append(lambda s: s.split(separator, 1)[-1])
        return self

    def strip_left_greedy(self, separator):
        self.strips.append(lambda s: s.rsplit(separator, 1)[-1])
        return self

    def strip_right(self, separator):
        self.strips.append(lambda s: s.rsplit(separator, 1)[0])
        return self

    def strip_right_greedy(self, separator):
        self.strips.append(lambda s: s.split(separator, 1)[0])
        return self

    def __call__(self, version):
        for strip in self.strips:
            version = strip(version)
        return version
