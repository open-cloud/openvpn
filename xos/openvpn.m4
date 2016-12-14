tosca_definitions_version: tosca_simple_yaml_1_0

# compile this with "m4 exampleservice.m4 > exampleservice.yaml"

# include macros
include(macros.m4)

node_types:
    tosca.nodes.OpenVPNService:
        derived_from: tosca.nodes.Root
        description: >
            OpenVPN Service
        capabilities:
            xos_base_service_caps
        properties:
            xos_base_props
            xos_base_service_props

    tosca.nodes.OpenVPNTenant:
        derived_from: tosca.nodes.Root
        description: >
            A Tenant of the OpenVPN service
        properties:
            xos_base_tenant_props

