import React from "react";
import { useIntl } from "react-intl";

export default function SortControl({ value = "", options = [], onChange = () => {}, id }) {
  const intl = useIntl();

  return (
    <div className="flex items-center gap-[10px]">
      <label
        htmlFor={id}
        className="text-[14px] leading-[22.4px] text-[#475569] whitespace-nowrap"
      >
        {intl.formatMessage({ id: "sortControl.label" })}
      </label>

      <select
        id={id}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="h-[41px] w-[156.5px] rounded-[8px] border border-[#CBD5E1] bg-white px-3 text-[14px] leading-[22.4px] text-[#475569] outline-none focus:ring-2 focus:ring-[#4361ee]/25 focus:border-[#4361ee]"
        aria-label="Sort products"
      >
        {options.length === 0 ? <option value="" /> : null}
        {options.map((opt) => (
          <option key={opt.value} value={opt.value}>
            {opt.label}
          </option>
        ))}
      </select>
    </div>
  );
}