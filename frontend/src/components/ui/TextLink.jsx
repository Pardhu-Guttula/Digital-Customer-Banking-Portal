import React from "react";
import { useIntl } from "react-intl";

export default function TextLink({ children, href = "#", onClick = () => {} }) {
  const intl = useIntl();

  return (
    <a
      href={href}
      onClick={(e) => onClick(e)}
      className="text-[14px] leading-5 font-normal tracking-[-0.1504px] text-[#155DFC] hover:underline focus:outline-none focus-visible:ring-2 focus-visible:ring-[#155DFC]/35 focus-visible:ring-offset-2 focus-visible:ring-offset-white rounded"
    >
      {children ?? intl.formatMessage({ id: "textLink.label" })}
    </a>
  );
}