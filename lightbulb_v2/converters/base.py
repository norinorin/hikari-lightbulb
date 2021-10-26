# -*- coding: utf-8 -*-
#
# This file is part of Lightbulb.
#
# Lightbulb is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Lightbulb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Lightbulb. If not, see <https://www.gnu.org/licenses/>.
from __future__ import annotations

__all__ = ["BaseConverter"]

import abc
import typing as t

from lightbulb_v2 import context as context_

T = t.TypeVar("T")


class BaseConverter(abc.ABC, t.Generic[T]):
    __slots__ = ("context",)

    def __init__(self, context: context_.base.Context) -> None:
        self.context = context

    @abc.abstractmethod
    def convert(self, arg: str) -> T:
        ...