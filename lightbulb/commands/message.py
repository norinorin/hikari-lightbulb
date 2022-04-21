# -*- coding: utf-8 -*-
# Copyright © tandemdude 2020-present
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

__all__ = ["MessageCommand"]

import typing as t

import hikari

from lightbulb.commands import base


class MessageCommand(base.ApplicationCommand):
    """
    An implementation of :obj:`~.commands.base.Command` representing a message context menu command.

    See the `API Documentation <https://discord.com/developers/docs/interactions/application-commands#message-commands>`_.
    """

    __slots__ = ()

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        super().__init__(*args, **kwargs)

    @property
    def options(self) -> t.Dict[str, t.Any]:
        return {}

    def _validate_attributes(self) -> None:
        if len(self.name) < 1 or len(self.name) > 32:
            raise ValueError(f"Message command {self.name!r}: name must be from 1-32 characters long") from None

    def as_create_kwargs(self) -> t.Dict[str, t.Any]:
        return {
            "type": hikari.CommandType.MESSAGE,
            "name": self.name,
        }
