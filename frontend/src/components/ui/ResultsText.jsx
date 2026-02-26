import React from "react";
import { useIntl } from "react-intl";

export default function ResultsText({ shownCount = 12, totalCount = 20 }) {
  const intl = useIntl();

  return (
    <p className="text-[14px] leading-[22.4px] text-[#475569] whitespace-nowrap">
      <span className="font-normal">
        {intl.formatMessage({ id: "resultsText.showingPrefix" })}{" "}
      </span>
      <span className="font-bold">{shownCount}</span>
      <span className="font-normal">
        {" "}
        {intl.formatMessage({ id: "resultsText.of" })}{" "}
      </span>
      <span className="font-bold">{totalCount}</span>
      <span className="font-normal">
        {" "}
        {intl.formatMessage({ id: "resultsText.productsSuffix" })}
      </span>
    </p>
  );
}