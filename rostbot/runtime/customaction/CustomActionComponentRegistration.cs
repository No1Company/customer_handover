using Microsoft.Bot.Builder;
using Microsoft.Bot.Builder.Dialogs.Debugging;
using Microsoft.Bot.Builder.Dialogs.Declarative;
using Microsoft.Bot.Builder.Dialogs.Declarative.Resources;
using Newtonsoft.Json;
using System.Collections.Generic;

namespace Microsoft.BotFramework.Composer.CustomAction
{
    public class CustomActionComponentRegistration : ComponentRegistration, IComponentDeclarativeTypes
    {
        public IEnumerable<DeclarativeType> GetDeclarativeTypes(ResourceExplorer resourceExplorer)
        {
            // Custom Actions
            yield return new DeclarativeType<AddThreeStrings>(AddThreeStrings.Kind);
            yield return new DeclarativeType<AddString>(AddString.Kind);
            yield return new DeclarativeType<TwoNumbers>(TwoNumbers.Kind);
            yield return new DeclarativeType<ConvertDate>(ConvertDate.Kind);

        }

        public IEnumerable<JsonConverter> GetConverters(ResourceExplorer resourceExplorer, SourceContext sourceContext)
        {
            yield break;
        }
    }
}