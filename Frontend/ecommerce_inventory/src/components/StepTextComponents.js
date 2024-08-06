import { Box, FormControl, FormControlLabel, InputLabel, MenuItem, Select, Switch, TextField } from '@mui/material';
import { useFormContext } from 'react-hook-form';

const StepTextComponents = ({formConfig, fieldType}) => {
    const {register, formState: {errors}} = useFormContext();
    const textFields = formConfig.data.text
    return (
        <Box>
            {textFields.map((field, index) => (
                <TextField 
                fullWidth
                margin='normal'
                key={field.name}
                label={field.label}
                error={!!errors[field.name]}
                defaultValue={field.default}
                placeholder={field.placeholder}
                {...register(field.name, {required:field.required})}
                />
            ))}
        </Box>
    )
}

export default StepTextComponents