#!/usr/bin/env python3
# MIT License
#
# Copyright (c) 2020 FABRIC Testbed
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#
# Author: Komal Thareja (kthare10@renci.org)
from fabric_cf.actor.core.manage.kafka.kafka_actor import KafkaActor
from fabric_mb.message_bus.messages.result_avro import ResultAvro


class Command:
    """
    Base class for varios commands
    """
    def __init__(self, *, logger):
        self.logger = logger

    @staticmethod
    def print_result(*, status: ResultAvro):
        print("Code={}".format(status.get_code()))
        if status.message is not None:
            print("Message={}".format(status.message))
        if status.details is not None:
            print("Details={}".format(status.details))

    @staticmethod
    def get_actor(*, actor_name: str) -> KafkaActor:
        from fabric_mgmt_cli.managecli.managecli import KafkaProcessorSingleton
        actor = KafkaProcessorSingleton.get().get_mgmt_actor(name=actor_name)
        return actor
