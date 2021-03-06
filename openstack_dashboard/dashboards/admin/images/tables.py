# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.utils.translation import ugettext_lazy as _

from horizon import tables

from openstack_dashboard.dashboards.project.images_and_snapshots \
        .images.tables import CreateImage
from openstack_dashboard.dashboards.project.images_and_snapshots \
        .images.tables import DeleteImage
from openstack_dashboard.dashboards.project.images_and_snapshots \
        .images.tables import EditImage
from openstack_dashboard.dashboards.project.images_and_snapshots \
        .images.tables import ImagesTable


class AdminCreateImage(CreateImage):
    url = "horizon:admin:images:create"


class AdminDeleteImage(DeleteImage):
    def allowed(self, request, image=None):
        if image and image.protected:
            return False
        else:
            return True


class AdminEditImage(EditImage):
    url = "horizon:admin:images:update"

    def allowed(self, request, image=None):
        return True


class AdminImagesTable(ImagesTable):
    name = tables.Column("name",
                         link="horizon:admin:images:detail",
                         verbose_name=_("Image Name"))

    class Meta:
        name = "images"
        verbose_name = _("Images")
        table_actions = (AdminCreateImage, AdminDeleteImage)
        row_actions = (AdminEditImage, AdminDeleteImage)
