import React from "react";
import { LayoutGrid, List } from "lucide-react";
import { useIntl } from "react-intl";
import IconToggleButton from "./IconToggleButton";

export default function ViewToggle({ value = "grid", onChange = () => {} }) {
  const intl = useIntl();

  return (
    <div className="flex items-center gap-[4px]" role="group" aria-label="View mode">
      <IconToggleButton
        active={value === "grid"}
        ariaLabel={intl.formatMessage({ id: "viewToggle.gridAria" })}
        icon={LayoutGrid}
        onClick={() => onChange("grid")}
      />
      <IconToggleButton
        active={value === "list"}
        ariaLabel={intl.formatMessage({ id: "viewToggle.listAria" })}
        icon={List}
        onClick={() => onChange("list")}
      />
    </div>
  );
}