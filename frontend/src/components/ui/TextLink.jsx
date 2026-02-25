import React from "react";
import { useIntl } from "react-intl";

function noop() {}

export default function TextLink({ label, onClick = noop }) {
  const intl = useIntl();
  const resolvedLabel = label ?? intl.formatMessage({ id: "textLink.label" });

  return (
    <button
      type="button"
      onClick={onClick}
      className="text-[14px] font-normal leading-5 tracking-[-0.1504px] text-[#155DFC] hover:underline focus:outline-none focus:ring-2 focus:ring-[#155DFC]/30 rounded"
    >
      {resolvedLabel}
    </button>
  );
}