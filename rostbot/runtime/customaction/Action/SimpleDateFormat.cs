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
    public class SimpleDateFormat : Dialog
    {
        [JsonConstructor]
        public SimpleDateFormat([CallerFilePath] string sourceFilePath = "", [CallerLineNumber] int sourceLineNumber = 0)
            : base()
        {
            // enable instances of this command as debug break point
            this.RegisterSourceLocation(sourceFilePath, sourceLineNumber);
        }

        [JsonProperty("$kind")]
        public const string Kind = "SimpleDateFormat";

        /// <summary>
        /// Gets or sets memory path to bind to arg1 (ex: conversation.width).
        /// </summary>
        /// <value>
        /// Memory path to bind to arg1 (ex: conversation.width).
        /// </value>
        [JsonProperty("simpledate")]
        public StringExpression SimpleDate { get; set; }

        /// <summary>
        /// Gets or sets caller's memory path to store the result of this step in (ex: conversation.area).
        /// </summary>
        /// <value>
        /// Caller's memory path to store the result of this step in (ex: conversation.area).
        /// </value>
        [JsonProperty("dateresult")]
        public StringExpression DateResult { get; set; }
        public override Task<DialogTurnResult> BeginDialogAsync(DialogContext dc, object options = null, CancellationToken cancellationToken = default(CancellationToken))
        {
            string inputdate = SimpleDate.GetValue(dc.State);
            int separatorIndex = inputdate.IndexOf(" ");
            string day = inputdate.Substring(0, separatorIndex);

            if (day.Length == 1)
            {
                day = "0" + day;
            }
            else if (day.Length > 2)
            {
                day = day.Substring(0, 2);
            }

            DateTime current = DateTime.Now;
            int year = current.Year;
            int curr_month = current.Month;
            string month_string = inputdate.Substring((separatorIndex + 1), (inputdate.Length - separatorIndex - 1));
            int month = 0;
            string[] monthsArray = { "januari", "februari", "mars", "april", "maj", "juni", "juli", "augusti", "september", "oktober", "november", "december" };
            month_string = month_string.ToLower();

            for (int i = 0; i < monthsArray.Length; i++)
            {
                if (month_string == monthsArray[i])
                {
                    month = (i + 1);
                    break;
                    
                } 
                else 
                {
                    month = 0;
                }
            }

            if(curr_month > month && month != 0)
            {
                year++;
            }

            string year_string = year.ToString().Substring(2, 2);
            month_string = month.ToString();

            if (month_string.Length == 1)
            {
                month_string = "0" + month_string;
            }

            string fulldate = year_string + "/" + month_string + "/" + day;

            if (this.DateResult != null)
            {
                dc.State.SetValue(this.DateResult.GetValue(dc.State), fulldate);
            }

            return dc.EndDialogAsync(result: fulldate, cancellationToken: cancellationToken);
        }
    }
}
