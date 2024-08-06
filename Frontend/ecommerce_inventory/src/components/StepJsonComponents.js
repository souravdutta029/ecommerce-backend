import { Box, FormControl, FormControlLabel, InputLabel, MenuItem, Select, Switch, TextField } from '@mui/material';
import { useFormContext } from 'react-hook-form';
import JsoninputComponent from './JsoninputComponent'

const StepJsonComponents = ({formConfig, fieldType}) => {
    const {register} = useFormContext();
    const jsonFields = formConfig.data.json
    return (
        <Box>
            {
                jsonFields.map((field, index) => (
                    <JsoninputComponent key={field.name} fields={field} />
                ))
            }
        </Box>
    )
}

export default StepJsonComponents