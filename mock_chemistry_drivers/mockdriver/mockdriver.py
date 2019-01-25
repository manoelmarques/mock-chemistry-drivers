# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

from qiskit.chemistry.drivers import BaseDriver
from qiskit.chemistry import QMolecule, QiskitChemistryError
import logging

logger = logging.getLogger(__name__)


class MockDriver(BaseDriver):
    """Mock driver."""

    CONFIGURATION = {
        "name": "MockDriver",
        "description": "Mocke Chemistry Driver",
        "input_schema": {
            "$schema": "http://json-schema.org/schema#",
            "id": "mockfriver_schema",
            "type": "string",
            "default": "Mock driver default input"
        }
    }

    def __init__(self, config):
        """
        Initializer
        Args:
            config (str or list): driver configuration
        """
        if not isinstance(config, list) and not isinstance(config, str):
            raise QiskitChemistryError("Invalid input for MockDriver Driver '{}'".format(config))

        if isinstance(config, list):
            config = '\n'.join(config)

        super().__init__()
        self._config = config

    @classmethod
    def init_from_input(cls, section):
        """
        Initialize via section dictionary.

        Args:
            params (dict): section dictionary

        Returns:
            Driver: Driver object
        """
        if 'data' not in section:
            raise QiskitChemistryError('Missing data section')

        kwargs = {'config': section['data']}
        logger.debug('init_from_input: {}'.format(kwargs))
        return cls(**kwargs)

    def run(self):
        return QMolecule()
