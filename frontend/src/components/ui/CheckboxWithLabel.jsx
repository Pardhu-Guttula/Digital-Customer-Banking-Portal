import React from "react";
import { useIntl } from "react-intl";

export default function CheckboxWithLabel({
  id,
  checked,
  onCheckedChange = () => {},
  label,
}) {
  const intl = useIntl();

  const resolvedLabel =
    label ?? intl.formatMessage({ id: "checkboxWithLabel.rememberMe" });

  return (
    <div className="flex items-center gap-2">
      <input
        id={id}
        type="checkbox"
        checked={checked}
        onChange={(e) => onCheckedChange(e.target.checked)}
        className="h-[13px] w-[13px] rounded-[3px] border border-[#cbd5e1] bg-white align-middle accent-[#155dfc]"
      />
      <label
        htmlFor={id}
        className="text-[16px] leading-6 font-medium tracking-[-0.3125px] text-[#4a5565] select-none cursor-pointer"
      >
        {resolvedLabel}
      </label>
    </div>
  );
}