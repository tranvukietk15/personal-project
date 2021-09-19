using System.Collections.Generic;
using IdentityServer4.Models;

namespace IdentityServer.Configs
{   
    public class IdpConfig
    {
        public static string Name => "IdpConfigs";
        public IEnumerable<Client> Clients { get; set; }
        public IEnumerable<ApiScope> ApiScopes { get; set; }
        public IEnumerable<IdentityResource> Resources { get; set; }
    }
}