using System;
using System.Runtime.CompilerServices;
using System.Threading;
using System.Threading.Tasks;
using AdaptiveExpressions.Properties;
using Microsoft.Bot.Builder.Dialogs;
using Newtonsoft.Json;

namespace Microsoft.BotFramework.Composer.CustomAction
{
    /// <summary>
    /// Custom command which takes takes 2 data bound arguments (arg1 and arg2) and multiplies them returning that as a databound result.
    /// </summary>
    public class ConvertDate : Dialog
    {
        [JsonConstructor]
        public ConvertDate([CallerFilePath] string sourceFilePath = "", [CallerLineNumber] int sourceLineNumber = 0)
            : base()
        {
            // enable instances of this command as debug break point
            this.RegisterSourceLocation(sourceFilePath, sourceLineNumber);
        }

        [JsonProperty("$kind")]
        public const string Kind = "ConvertDate";

        /// <summary>
        /// Gets or sets memory path to bind to InputString (ex: conversation.width).
        /// </summary>
        /// <value>
        /// Memory path to bind to InputString (ex: conversation.width).
        /// </value>
        [JsonProperty("InputString")]
        public StringExpression InputString { get; set; }

    
        /// <summary>
        /// Gets or sets caller's memory path to store the result of this step in (ex: conversation.area).
        /// </summary>
        /// <value>
        /// Caller's memory path to store the result of this step in (ex: conversation.area).
        /// </value>
        [JsonProperty("DateResult")]
        public StringExpression DateResult { get; set; }

        public override Task<DialogTurnResult> BeginDialogAsync(DialogContext dc, object options = null, CancellationToken cancellationToken = default(CancellationToken))
        {
           
           var result = InputString.GetValue(dc.State); 
          

            return dc.EndDialogAsync(result: result, cancellationToken: cancellationToken);
        }
    }
}
