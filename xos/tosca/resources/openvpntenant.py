from xosresource import XOSResource
from core.models import Tenant, Service
from services.openvpn.models import OpenVPNTenant


class XOSOpenVPNTenant(XOSResource):
    provides = "tosca.nodes.OpenVPNTenant"
    xos_model = OpenVPNTenant
    name_field = "service_specific_id"
    copyin_props = ("tenant_message",)

    def get_xos_args(self, throw_exception=True):
        args = super(XOSOpenVPNTenant, self).get_xos_args()

        # ExampleTenant must always have a provider_service
        provider_name = self.get_requirement("tosca.relationships.TenantOfService", throw_exception=True)
        if provider_name:
            args["provider_service"] = self.get_xos_object(Service, throw_exception=True, name=provider_name)

        return args

    def get_existing_objs(self):
        args = self.get_xos_args(throw_exception=False)
        return OpenVPNTenant.get_tenant_objects().filter(provider_service=args["provider_service"], service_specific_id=args["service_specific_id"])
        return []

    def can_delete(self, obj):
        return super(XOSOpenVPNTenant, self).can_delete(obj)

