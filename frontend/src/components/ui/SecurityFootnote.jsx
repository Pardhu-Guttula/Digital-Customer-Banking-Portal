import React from "react";
import { useIntl } from "react-intl";
import SecurityFootnoteText from "./SecurityFootnoteText";

export default function SecurityFootnote({ text, onClick = () => {} }) {
  const intl = useIntl();

  const resolvedText =
    text ?? intl.formatMessage({ id: "securityFootnote.defaultText" });

  return (
    <div className="flex flex-col items-center w-full">
      <button
        type="button"
        onClick={onClick}
        className="inline-flex items-center justify-center rounded-[6px] px-[6px] py-[2px] text-left focus:outline-none focus-visible:ring-2 focus-visible:ring-[#155dfc]/40 focus-visible:ring-offset-2 focus-visible:ring-offset-transparent"
        aria-label={resolvedText}
      >
        <SecurityFootnoteText text={resolvedText} />
      </button>
    </div>
  );
}