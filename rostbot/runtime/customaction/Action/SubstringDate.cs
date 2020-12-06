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
    public class SubstringDate : Dialog
    {
        [JsonConstructor]
        public SubstringDate([CallerFilePath] string sourceFilePath = "", [CallerLineNumber] int sourceLineNumber = 0)
            : base()
        {
            // enable instances of this command as debug break point
            this.RegisterSourceLocation(sourceFilePath, sourceLineNumber);
        }

        [JsonProperty("$kind")]
        public const string Kind = "SubstringDate";

        /// <summary>
        /// Gets or sets memory path to bind to arg1 (ex: conversation.width).
        /// </summary>
        /// <value>
        /// Memory path to bind to arg1 (ex: conversation.width).
        /// </value>
        [JsonProperty("fulldate")]
        public StringExpression FullDate { get; set; }

        /// <summary>
        /// Gets or sets caller's memory path to store the result of this step in (ex: conversation.area).
        /// </summary>
        /// <value>
        /// Caller's memory path to store the result of this step in (ex: conversation.area).
        /// </value>
        [JsonProperty("dateresult")]
        public StringExpression DateShort { get; set; }


        public override Task<DialogTurnResult> BeginDialogAsync(DialogContext dc, object options = null, CancellationToken cancellationToken = default(CancellationToken))
        {
            string dateString = FullDate.GetValue(dc.State);
            string dateShortString = dateString.Substring(0,8);

            if (this.DateShort != null)
            {
                dc.State.SetValue(this.DateShort.GetValue(dc.State), dateShortString);
            }
            return dc.EndDialogAsync(result: dateShortString, cancellationToken: cancellationToken);
        }
    }
}
