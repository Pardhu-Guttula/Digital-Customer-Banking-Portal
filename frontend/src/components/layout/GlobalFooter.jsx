import React from "react";
import { useIntl } from "react-intl";

export default function GlobalFooter({ text }) {
  const intl = useIntl();

  const resolvedText =
    text ?? intl.formatMessage({ id: "globalFooter.securityNote" });

  return (
    <footer className="text-center">
      <p className="text-sm leading-5 tracking-[-0.1504px] text-[#4a5565]">
        {resolvedText}
      </p>
    </footer>
  );
}