using Microsoft.Bot.Connector.Authentication;
using Microsoft.Extensions.Configuration;

namespace Microsoft.BotFramework.Composer.WebAppTemplates
{
    public class ConfigurationCredentialProvider : SimpleCredentialProvider
    {
        public ConfigurationCredentialProvider(IConfiguration configuration) 
            : base(configuration["MicrosoftAppid"], configuration["MicrosoftAppPassword"])
        {
        }
    }
}