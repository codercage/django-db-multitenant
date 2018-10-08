from db_multitenant import mapper

class TenantMapper(mapper.TenantMapper):
    def get_tenant_params(self, request):
        return {
            'host': '',
            'port': 3306,
            'db': '',
            'user': '',
            'passwd': '',
        }

    def get_cache_prefix(self, request, tenant_name, db_name):
        pass