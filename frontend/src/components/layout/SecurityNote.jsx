import React from "react";
import { useIntl } from "react-intl";

export default function SecurityNote({ text }) {
  const intl = useIntl();

  return (
    <footer aria-label={intl.formatMessage({ id: "securityNote.ariaLabel" })} className="w-full">
      <p className="m-0 text-center text-sm font-normal leading-5 text-[#4A5565]">{text}</p>
    </footer>
  );
}